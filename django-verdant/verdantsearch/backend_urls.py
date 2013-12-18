from django.conf.urls import patterns, url


urlpatterns = patterns("verdantsearch.views",
    url(r"^editorspicks/$", "editorspicks.index", name="verdantsearch_editorspicks_index"),
    url(r"^editorspicks/_add/$", "editorspicks.add", name="verdantsearch_editorspicks_add"),
    url(r"^editorspicks/(?P<slug>[a-z0-9-]+)/$", "editorspicks.edit", name="verdantsearch_editorspicks_edit"),
    url(r"^editorspicks/(?P<slug>[a-z0-9-]+)/delete/$", "editorspicks.delete", name="verdantsearch_editorspicks_delete"),
)