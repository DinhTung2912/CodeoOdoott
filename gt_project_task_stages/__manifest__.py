# -*- coding: utf-8 -*-
{
    "name": "Project Task Stages",
    "version": "16.0.1.0",
    "category": "Sale/Project",
    "summary": "Project Stages",
    "description": """Auto create project task stages""",
    "author": "Gritxi Technologies Pvt. Ltd.",
    "company": "Gritxi Technologies Pvt. Ltd.",
    "maintainer": "Gritxi Technologies Pvt. Ltd.",
    "images": ["static/description/banner.jpg"],
    "website": "https://www.gritxi-tech.com/",
    "depends": ['project', 'sale_management', 'sale_project'],
    "data": [
        "security/ir.model.access.csv",
        "views/task_stage_template_view.xml",
        "views/product_template_view.xml",
        "views/project_project_view.xml",
    ],
    "price": 15,
    "currency": "USD",
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "OPL-1",
}
