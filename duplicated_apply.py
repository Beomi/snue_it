import csv
import collections


print('서울교육대학교 학생 IT지원국에서 제작한\n임용고시 강의실 대여 중복처리 프로그램입니다.')
print('code by Junbum Lee')
print('문제가 있는 경우 jblee+help@student.snue.ac.kr로 문의주시기 바랍니다.')

file_name = input("사용하실 파일 이름을 입력해 주세요(~~.csv): ")
reader = csv.DictReader(open(file_name,encoding='utf8'))

result = {}
for row in reader:
    for column, value in row.items():
        result.setdefault(column, []).append(value)

result_all = result['스터디 장 학번'] + result['스터디 부원-1 학번'] + result['스터디 부원-2 학번'] + result['스터디 부원-3 학번'] + result['스터디 부원-4 학번'] + result['스터디 부원-5 학번'] + result['스터디 부원-6 학번']

result_name = result['스터디 장 이름'] + result['스터디 부원 -1 이름'] + result['스터디 부원-2 이름'] + result['스터디 부원-3 이름'] + result['스터디 부원-4 이름'] + result['스터디 부원-5 이름'] + result['스터디 부원-6 이름']


print('-' * 70)

print("아래 학번을 가진 사람들은 중복으로 신청한 사람입니다.")
print([item for item, count in collections.Counter(result_all).items() if count > 1])

print('-' * 70)

print("아래 이름을 가진 사람들은 중복으로 신청한 사람입니다.")
print([item for item, count in collections.Counter(result_name).items() if count > 1])

input("종료하시려면 엔터를 눌러주세요.")
