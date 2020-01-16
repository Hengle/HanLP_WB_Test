#! python3
# coding=gbk
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# 考试用的数据。键是州，值是州首府。
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
            'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 创建 35 份试卷。
for quizNum in range(3):

    # 创建考卷文件和答案文件
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')  # 创建考卷文件
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')  # 创建答案文件

    # 创建考卷头的内容
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')  # 考卷头：姓名，日期，班级
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))  # 考卷的唯一编号
    quizFile.write('\n\n')

    # 随机打乱题目的顺序
    states = list(capitals.keys())  # 获取州列表
    random.shuffle(states)  # 随机打乱周列表

    # 根据打乱顺序后的题目，创建答案选项
