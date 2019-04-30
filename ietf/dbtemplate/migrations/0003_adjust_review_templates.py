# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 11:39
from __future__ import unicode_literals

from django.db import migrations

def forward(apps, schema_editor):
    DBTemplate = apps.get_model('dbtemplate', 'DBTemplate')
    DBTemplate.objects.filter(id=186).update(content="""I am the assigned Gen-ART reviewer for this draft. The General Area
Review Team (Gen-ART) reviews all IETF documents being processed
by the IESG for the IETF Chair.  Please treat these comments just
like any other last call comments.

For more information, please see the FAQ at

<https://trac.ietf.org/trac/gen/wiki/GenArtfaq>.

Document: {{ assignment.review_request.doc.name }}-??
Reviewer: {{ assignment.reviewer.person.plain_name }}
Review Date: {{ today }}
IETF LC End Date: {% if assignment.review_request.doc.most_recent_ietflc %}{{ assignment.review_request.doc.most_recent_ietflc.expires|date:"Y-m-d" }}{% else %}None{% endif %}
IESG Telechat date: {{ assignment.review_request.doc.telechat_date|default:'Not scheduled for a telechat' }}

Summary:

Major issues:

Minor issues:

Nits/editorial comments:
""")

    DBTemplate.objects.filter(id=187).update(content="""I am the assigned Gen-ART reviewer for this draft. The General Area
Review Team (Gen-ART) reviews all IETF documents being processed
by the IESG for the IETF Chair. Please wait for direction from your
document shepherd or AD before posting a new version of the draft.

For more information, please see the FAQ at

<https://trac.ietf.org/trac/gen/wiki/GenArtfaq>.

Document: {{ assignment.review_request.doc.name }}-??
Reviewer: {{ assignment.reviewer.person.plain_name }}
Review Date: {{ today }}
IETF LC End Date: {% if assignment.review_req.doc.most_recent_ietflc %}{{ assignment.review_request.doc.most_recent_ietflc.expires|date:"Y-m-d" }}{% else %}None{% endif %}
IESG Telechat date: {{ assignment.review_request.doc.telechat_date|default:'Not scheduled for a telechat' }}

Summary:

Major issues:

Minor issues:

Nits/editorial comments:

""")

def reverse(apps, schema_editor):
    DBTemplate = apps.get_model('dbtemplate','DBTemplate')
    DBTemplate.objects.filter(id=186).update(content="""I am the assigned Gen-ART reviewer for this draft. The General Area
Review Team (Gen-ART) reviews all IETF documents being processed
by the IESG for the IETF Chair.  Please treat these comments just
like any other last call comments.

For more information, please see the FAQ at

<https://trac.ietf.org/trac/gen/wiki/GenArtfaq>.

Document: {{ review_req.doc.name }}-??
Reviewer: {{ review_req.reviewer.person.plain_name }}
Review Date: {{ today }}
IETF LC End Date: {% if review_req.doc.most_recent_ietflc %}{{ review_req.doc.most_recent_ietflc.expires|date:"Y-m-d" }}{% else %}None{% endif %}
IESG Telechat date: {{ review_req.doc.telechat_date|default:'Not scheduled for a telechat' }}

Summary:

Major issues:

Minor issues:

Nits/editorial comments:

""")
    DBTemplate.objects.filter(id=187).update(content="""I am the assigned Gen-ART reviewer for this draft. The General Area
Review Team (Gen-ART) reviews all IETF documents being processed
by the IESG for the IETF Chair. Please wait for direction from your
document shepherd or AD before posting a new version of the draft.

For more information, please see the FAQ at

<https://trac.ietf.org/trac/gen/wiki/GenArtfaq>.

Document: {{ review_req.doc.name }}-??
Reviewer: {{ review_req.reviewer.person.plain_name }}
Review Date: {{ today }}
IETF LC End Date: {% if review_req.doc.most_recent_ietflc %}{{ review_req.doc.most_recent_ietflc.expires|date:"Y-m-d" }}{% else %}None{% endif %}
IESG Telechat date: {{ review_req.doc.telechat_date|default:'Not scheduled for a telechat' }}

Summary:

Major issues:

Minor issues:

Nits/editorial comments:

""")

class Migration(migrations.Migration):

    dependencies = [
        ('dbtemplate', '0002_auto_20180220_1052'),
        ('doc','0011_reviewassignmentdocevent'),
    ]

    operations = [
        migrations.RunPython(forward, reverse)
    ]
