import sys,time

class Process_bar:
    data=0; #当前进度
    total=100; #总进度
    title="Undefine";  #显示进度标题

    def run(self):
        t_str=self.title
        if(len(self.title)>20):
            t_str=self.title[0:20]+'...'
            #这些是对进度标题的限制，超过20个的只能显示前20个字符的缩写
        while(self.data < self.total ):
            self.data=self.data+1 #本来应该是获得当前时间的进度数据
            percent=int(((self.data / self.total)*100)//1)
            str='='*percent+'_'*(100-percent)
            sys.stdout.write('\r'+t_str+' ['+str+']'+'  [%s%%]'%(percent))
            time.sleep(0.02) #为了体现进度条
            sys.stdout.flush()
        sys.stdout.write('\n')
        #End of function run()
  #End of Class Process_bar

#Demo
a=Process_bar()
a.title="正在初始化网络……"
a.run()

b=Process_bar()
b.title="How are you Indian Mi fan,do you like mi4i?"
b.total = 1000
b.run()
#END