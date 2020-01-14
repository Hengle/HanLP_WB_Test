#! python3
# coding=gbk

from pyhanlp import *

print(HanLP.segment('���ã���ӭ��Python�е���HanLP��API'))

for term in HanLP.segment('����������ˮ'):
    print('{}\t{}'.format(term.word, term.nature))  # ��ȡ���������

testCases = [
    "��Ʒ�ͷ���",
    "���ĺ���δ����ȷʵ�ڸ��ŷִʰ�",
    "��ˮ��Ȼ��������԰���ȥ������",
    "�й����׶��Ǳ���",
    "��ӭ����ʦ��ǰ���ò�",
    "��ӭ����ʦ��ǰ���Ͳ�",
    "���Ŵ�Ů����ÿ�¾����������Ҷ�Ҫ�׿ڽ���24�ڽ������ȼ����������İ�װ����",
    "����ά�ͷ���Ա",
    "����ҳ���������ڵ�ҳ�η�ʢ�������ڴ浵�����߼��жϵ���Ƽ����ˣ������Ҳ������ȫ���Ե���"]

for sentence in testCases:
    print(HanLP.segment(sentence))

document = "ˮ����ˮ��Դ˾˾��������9��29���ڹ���Ժ���Ű���е����ŷ�������͸¶��" \
           "���ݸո������ˮ��Դ�����ƶȵĿ��ˣ��в���ʡ�ӽ��˺��ߵ�ָ�꣬" \
           "�в���ʡ�������ߵ�ָ�ꡣ��һЩ�������ߵĵط��������ұ�ʾ����һЩȡ��ˮ��Ŀ���������������" \
           "�ϸ�ؽ���ˮ��Դ��֤��ȡˮ��ɵ���׼��"

# �ؼ�����ȡ
print(HanLP.extractKeyword(document, 2))

# �Զ�ժҪ
print(HanLP.extractSummary(document, 3))


def main():
    HanLP.Config.enableDebug()  # Ϊ�˱�����ȵ����ģ���������ģʽ˵��ʲô:-)
    # print(HanLP.segment("����ά�ͷ���Ա"))
    print(HanLP.parseDependency("�����������������ȷ���˰ѻ���ӥ���������ȸ��Ϊ����Ŀ��"))  # ����䷨����
    print(HanLP.parseDependency("������˵�������˽�ͬ���Ϲ����������˴��ģɱ���������ر�ίԱ��������ֺ�����"))  # ����䷨����


if __name__ == '__main__':
    main()
