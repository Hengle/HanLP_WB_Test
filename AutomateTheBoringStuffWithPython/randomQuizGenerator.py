#! python3
# coding=gbk
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# �����õ����ݡ������ݣ�ֵ�����׸���
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

# ���� 35 ���Ծ�
for quizNum in range(3):

    # ���������ļ��ʹ��ļ�
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')  # ���������ļ�
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')  # �������ļ�

    # ��������ͷ������
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')  # ����ͷ�����������ڣ��༶
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))  # �����Ψһ���
    quizFile.write('\n\n')

    # ���������Ŀ��˳��
    states = list(capitals.keys())  # ��ȡ���б�
    random.shuffle(states)  # ����������б�

    # ���ݴ���˳������Ŀ��������ѡ��
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]  # ��ȷ�Ĵ�
        wrongAnswers = list(capitals.values())  # 50 ��ԭʼ˳���ֵ���ɵ��б�
        del wrongAnswers[wrongAnswers.index(correctAnswer)]  # ������ȷ�Ĵ𰸣�����ֵ���ҵ�����������������ɾ�������
        wrongAnswers = random.sample(wrongAnswers, 3)  # ��ʣ�µĴ�����У����ѡ 3 ��
        answerOptions = wrongAnswers + [correctAnswer]  # �ϲ�����Ĵ𰸺ʹ���Ĵ𰸣�ע�⣬��ȷ�� �� �ַ��� תΪ �б�
        random.shuffle(answerOptions)  # ���Һϲ���Ĵ�

        # ����Ŀд���Ծ��ļ�
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))

        # ������ѡ��д���Ծ��ļ�
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # ����ȷ��д����ļ�
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()  # �ر��Ծ��ļ�
    answerKeyFile.close()  # �رմ��ļ�
