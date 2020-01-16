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
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]  # 正确的答案
        wrongAnswers = list(capitals.values())  # 50 个原始顺序的值构成的列表
        del wrongAnswers[wrongAnswers.index(correctAnswer)]  # 根据正确的答案，他是值，找到其索引，根据索引删除这个答案
        wrongAnswers = random.sample(wrongAnswers, 3)  # 在剩下的错误答案中，随机选 3 个
        answerOptions = wrongAnswers + [correctAnswer]  # 合并错误的答案和错误的答案，注意，正确答案 从 字符串 转为 列表
        random.shuffle(answerOptions)  # 打乱合并后的答案

        # 将题目写入试卷文件
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))

        # 将答题选项写入试卷文件
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # 将正确答案写入答案文件
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()  # 关闭试卷文件
    answerKeyFile.close()  # 关闭答案文件
