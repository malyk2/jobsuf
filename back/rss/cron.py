import feedparser
import re
# from rss.models import Job

from rss.models import Job, Country


# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# def get_temp_json()

def get_temp_entry1():
    return {'title': 'Virtual Assistant - Upwork', 'title_detail': {'type': 'text/plain', 'language': None, 'base': 'https://www.upwork.com/ab/feed/jobs/rss?api_params=1&amp;orgUid=839771403425337346&amp;paging=0%3B10&amp;q=laravel&amp;securityToken=27727d8977665574fe85a05a7e51bcc55ca3560306362f8e4acfc5b567964c71a635de2658fa9bc6755d778144230199e22274f056989da0e1bae49e5ed49c79&amp;sort=recency&amp;userUid=839771403425337344', 'value': 'Virtual Assistant - Upwork'}, 'links': [{'rel': 'alternate', 'type': 'text/html', 'href': 'https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss'}], 'link': 'https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss', 'summary': 'We are looking to hire an experienced Personal Assistant to help us keep growing. If you&#039;re hard-working and dedicated, Example Co. is an ideal place to get ahead. Apply today!<br />\nResponsibilities for Personal Assistant<br />\n* Answer phone calls received and direct them appropriately<br />\n* Record notes and messages for the client <br />\n* Perform as a liaison between the employer and household staff as required<br />\n* Act as the first point of contact for the employer as necessary<br />\n* Manage the employer&#039;s calendar and appointment scheduling<br />\n* Read and write correspondence in mail or email form<br />\nQualifications for Personal Assistant<br />\n* Proven experience working as a personal assistant required<br />\n* Proficient in computer technology especially Microsoft Office applications<br />\n* Excellent verbal and written communication skills<br />\n* Strong customer service and social skills<br />\n* Exceptional organizational and time-management skills<br />\n* Follows instructions clearly and accurately within a timely fashion<br />\n* Proactive and enthusiastic about delivering positive results.<br />\nHiring for immediate start thank you<br /><br /><b>Hourly Range</b>: $35.00-$50.00\n\n<br /><b>Posted On</b>: March 22, 2022 20:59 UTC<br /><b>Category</b>: General Virtual Assistance<br /><b>Skills</b>:Virtual Assistant,     Communications,     Email Communication,     Data Entry,     Phone Communication,     Selling    \n<br /><b>Skills</b>:        Virtual Assistant,                     Communications,                     Email Communication,                     Data Entry,                     Phone Communication,                     Selling            <br /><b>Location Requirement</b>: Only freelancers located in the United States may apply.\n<br /><b>Country</b>: United States\n<br /><a href="https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss">click to apply</a>', 'summary_detail': {'type': 'text/html', 'language': None, 'base': 'https://www.upwork.com/ab/feed/jobs/rss?api_params=1&amp;orgUid=839771403425337346&amp;paging=0%3B10&amp;q=laravel&amp;securityToken=27727d8977665574fe85a05a7e51bcc55ca3560306362f8e4acfc5b567964c71a635de2658fa9bc6755d778144230199e22274f056989da0e1bae49e5ed49c79&amp;sort=recency&amp;userUid=839771403425337344', 'value': 'We are looking to hire an experienced Personal Assistant to help us keep growing. If you&#039;re hard-working and dedicated, Example Co. is an ideal place to get ahead. Apply today!<br />\nResponsibilities for Personal Assistant<br />\n* Answer phone calls received and direct them appropriately<br />\n* Record notes and messages for the client <br />\n* Perform as a liaison between the employer and household staff as required<br />\n* Act as the first point of contact for the employer as necessary<br />\n* Manage the employer&#039;s calendar and appointment scheduling<br />\n* Read and write correspondence in mail or email form<br />\nQualifications for Personal Assistant<br />\n* Proven experience working as a personal assistant required<br />\n* Proficient in computer technology especially Microsoft Office applications<br />\n* Excellent verbal and written communication skills<br />\n* Strong customer service and social skills<br />\n* Exceptional organizational and time-management skills<br />\n* Follows instructions clearly and accurately within a timely fashion<br />\n* Proactive and enthusiastic about delivering positive results.<br />\nHiring for immediate start thank you<br /><br /><b>Hourly Range</b>: $35.00-$50.00\n\n<br /><b>Posted On</b>: March 22, 2022 20:59 UTC<br /><b>Category</b>: General Virtual Assistance<br /><b>Skills</b>:Virtual Assistant,     Communications,     Email Communication,     Data Entry,     Phone Communication,     Selling    \n<br /><b>Skills</b>:        Virtual Assistant,                     Communications,                     Email Communication,                     Data Entry,                     Phone Communication,                     Selling            <br /><b>Location Requirement</b>: Only freelancers located in the United States may apply.\n<br /><b>Country</b>: United States\n<br /><a href="https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss">click to apply</a>'}, 'content': [{'type': 'text/html', 'language': None, 'base': 'https://www.upwork.com/ab/feed/jobs/rss?api_params=1&amp;orgUid=839771403425337346&amp;paging=0%3B10&amp;q=laravel&amp;securityToken=27727d8977665574fe85a05a7e51bcc55ca3560306362f8e4acfc5b567964c71a635de2658fa9bc6755d778144230199e22274f056989da0e1bae49e5ed49c79&amp;sort=recency&amp;userUid=839771403425337344', 'value': 'We are looking to hire an experienced Personal Assistant to help us keep growing. If you&#039;re hard-working and dedicated, Example Co. is an ideal place to get ahead. Apply today!<br />\nResponsibilities for Personal Assistant<br />\n* Answer phone calls received and direct them appropriately<br />\n* Record notes and messages for the client <br />\n* Perform as a liaison between the employer and household staff as required<br />\n* Act as the first point of contact for the employer as necessary<br />\n* Manage the employer&#039;s calendar and appointment scheduling<br />\n* Read and write correspondence in mail or email form<br />\nQualifications for Personal Assistant<br />\n* Proven experience working as a personal assistant required<br />\n* Proficient in computer technology especially Microsoft Office applications<br />\n* Excellent verbal and written communication skills<br />\n* Strong customer service and social skills<br />\n* Exceptional organizational and time-management skills<br />\n* Follows instructions clearly and accurately within a timely fashion<br />\n* Proactive and enthusiastic about delivering positive results.<br />\nHiring for immediate start thank you<br /><br /><b>Hourly Range</b>: $35.00-$50.00\n\n<br /><b>Posted On</b>: March 22, 2022 20:59 UTC<br /><b>Category</b>: General Virtual Assistance<br /><b>Skills</b>:Virtual Assistant,     Communications,     Email Communication,     Data Entry,     Phone Communication,     Selling    \n<br /><b>Skills</b>:        Virtual Assistant,                     Communications,                     Email Communication,                     Data Entry,                     Phone Communication,                     Selling            <br /><b>Location Requirement</b>: Only freelancers located in the United States may apply.\n<br /><b>Country</b>: United States\n<br /><a href="https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss">click to apply</a>'}], 'published': 'Tue, 22 Mar 2022 20:59:37 +0000', 'id': 'https://www.upwork.com/jobs/Virtual-Assistant_%7E01b515af441f59d418?source=rss', 'guidislink': False}


def get_real_entries():
    NewsFeed = feedparser.parse("https://www.upwork.com/ab/feed/jobs/rss?api_params=1&amp;orgUid=839771403425337346&amp;paging=0%3B10&amp;q=laravel&amp;securityToken=27727d8977665574fe85a05a7e51bcc55ca3560306362f8e4acfc5b567964c71a635de2658fa9bc6755d778144230199e22274f056989da0e1bae49e5ed49c79&amp;sort=recency&amp;userUid=839771403425337344")
    # entry = NewsFeed.entries[1]
    return NewsFeed.entries


def load_rss_upwork():
    print('load_rss_upwork')

    # entries = get_real_entries()
    # for entry in entries:
    #     handle_entry(entry)

    entry = get_temp_entry1()
    handle_entry(entry)


def handle_entry(entry):
    upwork_id = entry['id']
    if not Job.objects.filter(upwork_id=upwork_id).exists():
        content = entry['content'][0]['value']
        data = {
            'title': entry['title'],
            'content': content,
            'upwork_id': entry['id'],
            'country': get_country(content),
        }
        Job.objects.create(**data)


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


def get_new_line_pattern(keyword):
    return f'.*(\\n.*{keyword}<\/b>:)(.*)\\n'
