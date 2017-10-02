# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "elvaapp"
app_title = "ElvaApp"
app_publisher = "ovresko tech"
app_description = "Gestion elvage"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "ovresko@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/elvaapp/css/elvaapp.css"
# app_include_js = "/assets/elvaapp/js/elvaapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/elvaapp/css/elvaapp.css"
# web_include_js = "/assets/elvaapp/js/elvaapp.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "elvaapp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "elvaapp.install.before_install"
# after_install = "elvaapp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "elvaapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }
calendars = ["Insemination"]

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
 	"Insemination": {
 		"after_insert": "elvaapp.reproduction.stat_controller.insemination_event"
    },
    "Diagnostique":{
        "after_insert": "elvaapp.reproduction.stat_controller.diagnostique_event"
    },
    "Velage": {
        "after_insert": "elvaapp.reproduction.stat_controller.velage_event"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"elvaapp.tasks.all"
# 	],
# 	"daily": [
# 		"elvaapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"elvaapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"elvaapp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"elvaapp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "elvaapp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "elvaapp.event.get_events"
# }
