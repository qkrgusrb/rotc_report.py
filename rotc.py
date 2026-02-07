me = input("당신의 이름을 적으시오==>")
date = input("날짜를 입력하시오 ex : 2/20 (금)==>")
event = input("보고사항 ex) 동아대학교 신입생 OT 참석인원==>")

attendees = []
while True:
    name = input("참여하는 후보생 이름을 입력하세요(종료하려면 '끝' 입력)==>")
    if name == "끝":
        break
    attendees.append(name)

attendees.sort()
name_string = ", ".join(attendees) + "후보생"

absentees_dict = {}
while True:
    n_name = input("열외하는 후보생 이름을 입력하세요(종료하려면 '끝' 입력)==>")
    if n_name == "끝":
        break

    n_name_list = n_name.split()
    n_name_list.sort()

    reason = input(f"'{', '.join(n_name_list)}' 후보생의 열외 사유를 입력하시오==>")

    if reason in absentees_dict:
        absentees_dict[reason].extend(n_name_list)
    else:
        absentees_dict[reason] = n_name_list

    absentees_dict[reason].sort()

all_absentees = []
for names in absentees_dict.values():
    all_absentees.extend(names)
all_absentees.sort()
n_name_string = ", ".join(all_absentees) + "후보생"

print(f"\n충성!! {me}후보생입니다.")
print(f"{date} {event} 보고드리겠습니다.\n")
print(f"참석 ({len(attendees)}명) : {name_string}\n")
print(f"열외 ({len(all_absentees)}명) : {n_name_string}\n")
print("열외사유\n")

for reason in sorted(absentees_dict.keys()):
    names = absentees_dict[reason]
    print(f"{reason} ({len(names)}명) : {', '.join(names)}후보생\n")

print("이상입니다.")




