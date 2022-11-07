class PriorityQueueSortedList:
    def __init__(self):
        self.sorted_list = []
        self.size = 0

    def add(self, item, priority):
        self.sorted_list.append([item, priority])
        self.size += 1

    def update(self, new_priority, item):
        for i in range(self.size):
            if item == self.sorted_list[i][0]:
                self.sorted_list[i][1] = new_priority
                break

    def remove(self):
        high_priority = self.sorted_list[0][1]
        index_priority = -1

        for i in range(self.size):
            if high_priority > self.sorted_list[i][1]:
                high_priority = self.sorted_list[i][1]
                index_priority = i
        
        self.sorted_list.pop(index_priority)
        self.size -= 1

    def removePriority(self, priority):
        for i in range(self.size):
            if priority == self.sorted_list[i][1]:
                self.sorted_list.pop(i)
                break
        
        self.size -= 1

    def peek(self):
        high_priority = self.sorted_list[0][1]
        index_priority = 0

        for i in range(self.size):
            if high_priority > self.sorted_list[i][1]:
                high_priority = self.sorted_list[i][1]
                index_priority = i
        
        print(f'Data prioritas tertinggi: (\'{self.sorted_list[index_priority][0]}\', {self.sorted_list[index_priority][1]})')

    def printIsiQueue(self):
        print("Isi Semua Queue: ", end="")
        for i in range(self.size):
            item = self.sorted_list[i][0]
            priority = self.sorted_list[i][1]
            
            print(f"('{item}', {priority})", end='')
            if i != self.size - 1:
                print(', ', end='')
        print()

sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()