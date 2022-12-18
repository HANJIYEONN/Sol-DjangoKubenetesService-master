from django.urls import path
from . import views


def x(c, m):
    return {
        "callback": c
        , "mapper": m
    }


urlpatterns = [
    #################################################
    # web browser 접근 가능 URL ( 즉, Client 접근 가능 )
    #################################################
    # listing
    # TODO: listing 구현 필요.
    # path('', views.validate, x("list_policies", "PoliciesMapper"))
    # , path('list', views.validate, x("list_policies", "PoliciesMapper"))

    # create
    # TODO: create form 구현 필요.
    # , path("add", views.validate, x("create_form_policy", "CreateMapper"))
    # , path("add-form", views.validate, x("create_form_policy", "CreateMapper"))
    # , path("create", views.validate, x("create_form_policy", "CreateMapper"))
    # , path("create-form", views.validate, x("create_form_policy", "CreateMapper"))

    # upgrade
    # TODO: upgrade form 구현 필요.
    # , path("edit", views.validate, x("edit_form_policy", "CreateMapper"))
    # , path("edit-form", views.validate, x("edit_form_policy", "CreateMapper"))
    # , path("upgrade", views.validate, x("edit_form_policy", "CreateMapper"))
    # , path("upgrade-form", views.validate, x("edit_form_policy", "CreateMapper"))
    #################################################


    #################################################
    # web browser 접근 불가 API ( 즉, Client 접근 불가 )
    #################################################
    # TODO: create API 구현 필요.
    # , path("api/create", views.validate, x("create_policy", "CreateMapper"))
    # TODO: edit API 구현 필요.
    # , path("api/edit", views.validate, x("edit_policy", "CreateMapper"))
    #################################################


    #################################################
    # web browser 접근 가능 API ( 즉, Client 접근 가능 )
    #################################################
    # TODO: group delete 구현 필요.
    # group delete 지원 ( wildcard:&, ex> aa&bb&cc/delete )
    # , path("<str:names>/delete", views.validate, x("delete_policies", "PoliciesMapper"))
    # TODO: serach 구현 필요.
    # , path('<str:search>/search', views.validate, x("search_policy", "PoliciesMapper"))
    #################################################


    #################################################
    # ajax support
    #################################################

    #################################################
]