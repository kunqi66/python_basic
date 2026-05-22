import datetime
class TodaList:
    total_tasks = 0
    total_complete_tasks = 0
    def __init__(self, owner ,task_type ,task, create_time = datetime.datetime.now()):
        self.owner = owner
        self.task_type = task_type
        self.tasks =[]
        self.tasks.append({'task':task,'completed':False})
        TodaList.total_tasks += 1
        
    def show(self):
        print(f'{self.owner}   {self.task_type}   {self.tasks}')
    def add_task(self, task):
        for item in self.tasks:
            if item['task'] == task:
                print('任务重复')
                return
        self.tasks.append({'task':task,'completed':False})
        TodaList.total_tasks += 1
    def comolete_task(self, task):
        for index in range(len(self.tasks)):
            if self.tasks[index]['task'] == task:
                self.tasks[index]['completed']  = True
                TodaList.total_complete_tasks += 1
    def show_tasks(self, show_all=True):
        if show_all:
            for item in self.tasks:
                print(f'{item['task']}{'完成了' if item['completed'] else '没完成'}')
        else:
            print(f'未完成的任务有:{[item['task'] for item in self.tasks if not item['completed']]}')
    def delete_task(self, task):
        for index in range(len(self.tasks)):
            if self.tasks[index]['task'] == task:
                del self.tasks[index]
                TodaList.total_tasks -= 1
    def get_progress(self):
        com_num = 0
        for item in self.tasks:
            if item['completed'] == True:
                com_num += 1
        return str(com_num/len(self.tasks)*100)+'%'
    @classmethod
    def get_total_tasks(cls):
        return cls.total_tasks
    @classmethod
    def get_total_progress(cls):
        return str(cls.total_complete_tasks/cls.total_tasks*100)+'%'

    @staticmethod
    def is_valid_task(task_name):
        return 1 <= task_name <= 50
    

if __name__ == '__main__':
    a = TodaList('myself','工作','写作业')

    a.add_task('做晨练')
    a.show_tasks()
    a.show()
    a.comolete_task('写作业')
    a.show_tasks(False)
    print(a.get_progress())
    print(TodaList.get_total_progress())
    a.delete_task('做晨练')
    print('---------分割----------')
    a.show_tasks()
    a.show()
