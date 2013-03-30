from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysamsung.views.home', name='home'),
	(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', 'mysamsung.views.home'),
    url(r'^login', 'mysamsung.views.login'),
    url(r'^show_main_page', 'mysamsung.views.show_main_page'),
    url(r'^save_customer', 'mysamsung.views.save_customer'),
    url(r'^save_supplier', 'mysamsung.views.save_supplier'),
    url(r'^save_employee', 'mysamsung.views.save_employee'),
    url(r'^save_sale_item', 'mysamsung.views.save_sale_item'),
    url(r'^delete_sale_item', 'mysamsung.views.delete_sale_item'),
    url(r'^show_edit_form', 'mysamsung.views.show_edit_form'),
    url(r'^do_query', 'mysamsung.views.do_query'),
    url(r'^help', 'mysamsung.views.help'),
    # url(r'^mysamsung/', include('mysamsung.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
