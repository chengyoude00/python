def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum


#����calc_sum()��û�м������������Ƿ��غ���
#f = calc_sum([1, 2, 3, 4])
#f
#�Ժ������е���ʱ���ż�������
#f()
#10
#���ڿ��Է��غ��������ǿ����ں���������Ϳ��Ծ���Ҫ��Ҫ���øú���
