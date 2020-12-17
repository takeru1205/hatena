class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyDict:
    def __init__(self):
        self.table = [None] * 1000

    def hash(self, key):
        # 1000で割った余りをhash値として扱う
        return key % 1000

    def add(self, key, value):
        hashed_key = self.hash(key)
        if self.table[hashed_key]:  # すでにキーにデータが存在したら
            ll = self.table[hashed_key]  # すでに存在しているデータ(連結リストの先頭)
            while ll:  # 連結リストの最後尾までループして，最後にデータを追加する
                if not ll.next:  # 連結リストの最後の場合
                    ll.next = LinkedList(value)  # 新しい値を連結リストに連結
                    break
                else:
                    ll = ll.next
        else:
            self.table[hashed_key] = LinkedList(value)  # データが既に存在していない場合，連結リストとしてデータを挿入

    def get(self, key):
        values = []
        hashed_key = self.hash(key)
        ll = self.table[hashed_key]
        if not ll:  # 指定したキーにデータが存在しない場合は-1を返す
            return -1
        while ll:  # 連結リストが存在する場合
            values.append(ll.value)  # 連結リストの値をリストに追加
            if not ll.next:  # もし連結リストの最後尾だったら
                return values
            else:
                ll = ll.next

    def remove(self, key, value):
        hashed_key = self.hash(key)
        ll = self.table[hashed_key]
        if not ll:  # 指定したキーにデータが存在しなかったら
            print('No Data')
            return
        if ll.value == value:  # 連結リストの先頭を削除する場合
            if ll.next:  # 先頭を削除して，連結リストを一つ前にずらす
                self.table[hashed_key] = ll.next
            else:  # データが一つだけの場合
                self.table[hashed_key] = None
            print(f'Key:{key}, Value:{value} Removed')
            return
        ll_prev = ll
        ll = ll_prev.next
        while ll:  # 指定したキーに複数連結リストが存在する場合
            if ll.value == value:
                ll_prev.next = ll.next
                print(f'Key:{key}, Value:{value} Removed')
                return
            else:
                ll_prev = ll
                ll = ll.next
        print('Data not Found')

if __name__ == '__main__':
    dictionary = MyDict()
    dictionary.add(1, 'orange')
    dictionary.add(2, 'apple')
    dictionary.add(3, 'grape')
    dictionary.add(1001, 'mikan')
    dictionary.add(1003, 'muscat')
    dictionary.add(2002, 'green apple')
    dictionary.add(3002, 'pineapple')
    dictionary.add(1004, 'melon')

    for i in range(1, 5):
        print(f'Key: {i}, Value: {dictionary.get(i)}')

    dictionary.remove(1, 'orange')
    dictionary.remove(2002, 'green apple')
    dictionary.remove(1003, 'muscat')

    for i in range(1, 5):
        print(f'Key: {i}, Value: {dictionary.get(i)}')


