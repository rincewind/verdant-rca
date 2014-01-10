from django.conf.urls import patterns, url


urlpatterns = patterns("verdantsearch.views",
    url(r"^editorspicks/$", "editorspicks.index", name="verdantsearch_editorspicks_index"),
    url(r"^editorspicks/add/$", "editorspicks.add", name="verdantsearch_editorspicks_add"),
    url(r"^editorspicks/(\d+)/$", "editorspicks.edit", name="verdantsearch_editorspicks_edit"),
    url(r"^editorspicks/(\d+)/delete/$", "editorspicks.delete", name="verdantsearch_editorspicks_delete"),

    url(r"^queries/chooser/$", "queries.chooser", name="verdantsearch_queries_chooser"),
    url(r"^queries/chooser/results/$", "queries.chooserresults", name="verdantsearch_queries_chooserresults"),
)
