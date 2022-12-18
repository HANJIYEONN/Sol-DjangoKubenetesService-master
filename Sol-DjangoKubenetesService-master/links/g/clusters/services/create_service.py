from common import constants as CC
from common.error.dummy import DummyError
from core.example.rancher_caller_example import RancherCallerExample

from .create.create_executor import CreateExecutor


class CreateService:

    def __new__(cls):
        """
        새로운 instance 생성을 요청할 시, 자신이 소유하고 있는 instance를 반환한다.\n
        없을시, 새로 생성하여 반환한다.
        """

        if not hasattr(cls, '_me'):
            # instance 생성.
            cls._me = super(CreateService, cls).__new__(cls)
            # 해당 instance의 필수 요구 member를 생성.
            cls._me.__caller = RancherCallerExample()
            cls._me.__creator = CreateExecutor()

        return cls._me

    def request_mapping(self, func_name, payload):

        # 받은 function 이름을 protected 이름으로 변경.
        prot_name = "_" + func_name
        if not hasattr(self._me, prot_name):
            raise Exception(self._me.__class__.__name__ + " object has no attribute '" + func_name + "'")

        # protected 처리된 function을 호출.
        reflect_func = getattr(self._me, prot_name)

        # 인수로 받은 option 값이 없는 경우.
        if payload is None:
            raise Exception("[payload] does not exist.")

        # 현재 Rancher API의 Schema가 cluster에 맞추어져 있는지 확인.
        self._me.__caller.evaluate_schema_if_invalid_do_update("global", "")

        # option 습득.
        options = {"me": "true"} \
            if CC.OPTIONS_STRING not in payload \
            else payload[CC.OPTIONS_STRING]

        return reflect_func(options)

    def _create_cluster(self, options):

        # cluster 생성.
        create_cluster_result = self._me.__caller.create_cluster(options)

        # 생성된 cluster로부터 id 추출.
        created_cluster_id = create_cluster_result["id"]

        # cluster의 token 생성.
        create_cluster_registration_token_result = self._me.__caller.create_cluster_registration_token(
            {"clusterId": created_cluster_id, "type": "clusterRegistrationToken"}
        )

        model = self._me.__creator.create_cluster(
            create_cluster_result
            , create_cluster_registration_token_result
        )

        return model
