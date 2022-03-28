import feedparser
import re
import datetime
from urllib import parse
from django.conf import settings
# import re
# from rss.models import Job

from rss.models import Job, Country, Upwork, Skill


# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# def get_temp_json()

def get_temp_entry1():
    return {'title': 'Virtual Assistant - Upwork', 'title_detail': {'type': 'text/plain', 'language': None, 'base': 'https://www.upwork.com/ab/feed/jobs/rss?api_params=1&amp;orgUid=839771403425337346&amp;paging=0%3B10&amp;q=laravel&amp;securityToken=27727d8977665574fe85a05a7e51bcc55ca3560306362f8e4acfc5b567964c71a635de2658fa9bc6755d778144230199e22274f056989da0e1bae49e5ed49c79&amp;sort=recency&amp;userUid=839771403425337344', 'value': 'Virtual Assistant - Upwork'}, 'links': [{'rel': 'alternate', 'type': 'text/html', 'href': 'https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss'}], 'link': 'https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss', 'summary': 'We are looking to hire an experienced Personal Assistant to help us keep growing. If you&#039;re hard-working and dedicated, Example Co. is an ideal place to get ahead. Apply today!<br />\nResponsibilities for Personal Assistant<br />\n* Answer phone calls received and direct them appropriately<br />\n* Record notes and messages for the client <br />\n* Perform as a liaison between the employer and household staff as required<br />\n* Act as the first point of contact for the employer as necessary<br />\n* Manage the employer&#039;s calendar and appointment scheduling<br />\n* Read and write correspondence in mail or email form<br />\nQualifications for Personal Assistant<br />\n* Proven experience working as a personal assistant required<br />\n* Proficient in computer technology especially Microsoft Office applications<br />\n* Excellent verbal and written communication skills<br />\n* Strong customer service and social skills<br />\n* Exceptional organizational and time-management skills<br />\n* Follows instructions clearly and accurately within a timely fashion<br />\n* Proactive and enthusiastic about delivering positive results.<br />\nHiring for immediate start thank you<br /><br /><b>Hourly Range</b>: $35.00-$50.00\n\n<br /><b>Posted On</b>: March 22, 2022 20:59 UTC<br /><b>Category</b>: General Virtual Assistance<br /><b>Skills</b>:Virtual Assistant,     Communications,     Email Communication,     Data Entry,     Phone Communication,     Selling    \n<br /><b>Skills</b>:        Virtual Assistant,                     Communications,                     Email Communication,                     Data Entry,                     Phone Communication,                     Selling            <br /><b>Location Requirement</b>: Only freelancers located in the United States may apply.\n<br /><b>Country</b>: United States\n<br /><a href="https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss">click to apply</a>', 'summary_detail': {'type': 'text/html', 'language': None, 'base': 'https://www.upwork.com/ab/feed/jobs/rss?api_params=1&amp;orgUid=839771403425337346&amp;paging=0%3B10&amp;q=laravel&amp;securityToken=27727d8977665574fe85a05a7e51bcc55ca3560306362f8e4acfc5b567964c71a635de2658fa9bc6755d778144230199e22274f056989da0e1bae49e5ed49c79&amp;sort=recency&amp;userUid=839771403425337344', 'value': 'We are looking to hire an experienced Personal Assistant to help us keep growing. If you&#039;re hard-working and dedicated, Example Co. is an ideal place to get ahead. Apply today!<br />\nResponsibilities for Personal Assistant<br />\n* Answer phone calls received and direct them appropriately<br />\n* Record notes and messages for the client <br />\n* Perform as a liaison between the employer and household staff as required<br />\n* Act as the first point of contact for the employer as necessary<br />\n* Manage the employer&#039;s calendar and appointment scheduling<br />\n* Read and write correspondence in mail or email form<br />\nQualifications for Personal Assistant<br />\n* Proven experience working as a personal assistant required<br />\n* Proficient in computer technology especially Microsoft Office applications<br />\n* Excellent verbal and written communication skills<br />\n* Strong customer service and social skills<br />\n* Exceptional organizational and time-management skills<br />\n* Follows instructions clearly and accurately within a timely fashion<br />\n* Proactive and enthusiastic about delivering positive results.<br />\nHiring for immediate start thank you<br /><br /><b>Hourly Range</b>: $35.00-$50.00\n\n<br /><b>Posted On</b>: March 22, 2022 20:59 UTC<br /><b>Category</b>: General Virtual Assistance<br /><b>Skills</b>:Virtual Assistant,     Communications,     Email Communication,     Data Entry,     Phone Communication,     Selling    \n<br /><b>Skills</b>:        Virtual Assistant,                     Communications,                     Email Communication,                     Data Entry,                     Phone Communication,                     Selling            <br /><b>Location Requirement</b>: Only freelancers located in the United States may apply.\n<br /><b>Country</b>: United States\n<br /><a href="https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss">click to apply</a>'}, 'content': [{'type': 'text/html', 'language': None, 'base': 'https://www.upwork.com/ab/feed/jobs/rss?api_params=1&amp;orgUid=839771403425337346&amp;paging=0%3B10&amp;q=laravel&amp;securityToken=27727d8977665574fe85a05a7e51bcc55ca3560306362f8e4acfc5b567964c71a635de2658fa9bc6755d778144230199e22274f056989da0e1bae49e5ed49c79&amp;sort=recency&amp;userUid=839771403425337344', 'value': 'We are looking to hire an experienced Personal Assistant to help us keep growing. If you&#039;re hard-working and dedicated, Example Co. is an ideal place to get ahead. Apply today!<br />\nResponsibilities for Personal Assistant<br />\n* Answer phone calls received and direct them appropriately<br />\n* Record notes and messages for the client <br />\n* Perform as a liaison between the employer and household staff as required<br />\n* Act as the first point of contact for the employer as necessary<br />\n* Manage the employer&#039;s calendar and appointment scheduling<br />\n* Read and write correspondence in mail or email form<br />\nQualifications for Personal Assistant<br />\n* Proven experience working as a personal assistant required<br />\n* Proficient in computer technology especially Microsoft Office applications<br />\n* Excellent verbal and written communication skills<br />\n* Strong customer service and social skills<br />\n* Exceptional organizational and time-management skills<br />\n* Follows instructions clearly and accurately within a timely fashion<br />\n* Proactive and enthusiastic about delivering positive results.<br />\nHiring for immediate start thank you<br /><br /><b>Hourly Range</b>: $35.00-$50.00\n\n<br /><b>Posted On</b>: March 22, 2022 20:59 UTC<br /><b>Category</b>: General Virtual Assistance<br /><b>Skills</b>:Virtual Assistant,     Communications,     Email Communication,     Data Entry,     Phone Communication,     Selling    \n<br /><b>Skills</b>:        Virtual Assistant,                     Communications,                     Email Communication,                     Data Entry,                     Phone Communication,                     Selling            <br /><b>Location Requirement</b>: Only freelancers located in the United States may apply.\n<br /><b>Country</b>: United States\n<br /><a href="https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss">click to apply</a>'}], 'published': 'Tue, 22 Mar 2022 20:59:37 +0000', 'id': 'https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss', 'guidislink': False}

def load_rss_upwork():
    print('load_rss_upwork')
    rsss = get_user_rss()
    print('rsss:' + str(len(rsss)))
    print(rsss)
    for user_rss in rsss:
        rss_url = get_rss_url(user_rss)
        entries = get_entries(rss_url)
        print(f'Count entries: {entries.count()}')

        for entry in entries:
            handle_entry(user_rss, entry)
    print(f'Count RSSs: {rsss.count()}')


def get_user_rss():
    print('get_user_rss')
    return Upwork.objects.filter(active=True, user__rss_secret__isnull=False).select_related('user').prefetch_related('user', 'user__rss_secret').exclude().all()


def get_rss_url(user_rss):
    url = f'https://www.upwork.com/ab/feed/{user_rss.type}/rss?'
    user_secret = user_rss.user.rss_secret
    params = {
        'orgUid': user_secret.org_uid,
        'securityToken': user_secret.security_token,
        'userUid': user_secret.user_uid,
    }

    if user_rss.type == 'topics':
        params['topic'] = user_rss.topic
    elif user_rss.type == 'jobs':
        params['api_params'] = 1
        params['sort'] = 'recency'
        params['q'] = user_rss.q

    url += parse.urlencode(params)

    return url


def get_entries(rss_url):
    NewsFeed = feedparser.parse(rss_url)
    return NewsFeed.entries


def handle_entry(user_rss, entry):
    upwork_id = entry['id']
    if not Job.objects.filter(upwork_id=upwork_id).exists():
        content = entry['content'][0]['value']
        data = {
            'rss': user_rss,
            'title': entry['title'],
            'content': content,
            'upwork_id': entry['id'],
            'country': get_country(content),
            'published': parse_published_date(entry['published']),
            'budget': get_budget(content),
        }
        rates = get_rates(content)
        if rates:
            data = {**data, **rates}

        job = Job.objects.create(**data)        # skill_names =
        skill_ids = get_skill_ids(get_skill_names(content))
        job.skills.set(skill_ids)


def get_country(content):
    pattern = get_new_line_pattern('Country')
    match = re.search(pattern, content)
    if match:
        country_name = match.group(2).strip()
        return first_or_create_country(country_name)
    else:
        return None


def first_or_create_country(country_name):
    exists = Country.objects.filter(name=country_name).first()
    return exists and exists or Country.objects.create(name=country_name)


def get_budget(content):
    pattern = get_new_line_pattern('Budget')
    match = re.search(pattern, content)
    if match:
        match_budget = re.search('^\$([\d,]*)', match.group(2).strip())
        if match_budget:
            return match_budget.group(1).replace(',', '')
    return None


def get_skill_names(content):
    pattern = get_new_line_pattern('Skills')
    match = re.search(pattern, content)
    if match:
        skills_str = match.group(2).strip()
        return [skill.strip() for skill in skills_str.split(',')]
    else:
        return None


def get_skill_ids(skill_names):
    skill_ids = []
    if skill_names:
        for skill_name in skill_names:
            skill, created = Skill.objects.get_or_create(name=skill_name)
            skill_ids.append(skill.id)
    return skill_ids


def get_rates(content):
    match = re.search(get_new_line_pattern('Hourly Range'), content)
    if match:
        rates_str = match.group(2).strip()
        match_from_to = re.search('^\$(\d.\.00)-\$(\d.\.00)', rates_str)
        if match_from_to:
            return {
                'rate_from': match_from_to.group(1).strip(),
                'rate_to': match_from_to.group(2).strip()
            }
    return None


def parse_published_date(date_str):
    date_format = '%a, %d %b %Y %H:%M:%S %z'
    try:
        return datetime.datetime.strptime(date_str, date_format)
    except:
        return None


def get_new_line_pattern(keyword):
    return f'.*(\\n.*{keyword}<\/b>:)(.*)\\n'
