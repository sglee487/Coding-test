import re

def solution(new_id):
    fix_id = new_id.lower()
    fix_id = re.sub('[~!@#$%^&*()=+\[{\]}:?,<>/]','',fix_id)
    fix_id = re.sub('(\.+)', '.', fix_id)
    fix_id = re.sub("^\.|\.$", '', fix_id)
    if fix_id == '': fix_id = 'a'
    fix_id = fix_id[:15]
    fix_id = re.sub("\.$", '', fix_id)
    while len(fix_id) <= 2:
        fix_id += fix_id[-1]
    return fix_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))