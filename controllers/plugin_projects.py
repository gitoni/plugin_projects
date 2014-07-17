# -*- coding: utf-8 -*-


def download():
    return response.download(request, db)


def projects():
    projects = db(db.plugin_projects_projects).select()
    topic = T("Projects")
    topic_description = "Some of my projects"
    return dict(topic = topic, topic_description = topic_description, projects = projects)


@auth.requires_membership("manager")
def manage_projects():
    grid = SQLFORM.grid(db.plugin_projects_projects)
    return locals()

def project_image():
    project = db.plugin_projects_projects[request.args(0)]
    return dict(item = project)
