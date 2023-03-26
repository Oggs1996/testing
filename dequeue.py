from collections import deque


def person_is_a_seller(name):
    if name[-1] == 'm':
        return True


def search_name(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_a_seller(person):
                print(person + ' is a seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
                print(search_queue)
                print(searched)

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'johny']
graph['anuj'] = []
graph['peggy'] = ['nic']
graph['thom'] = []
graph['johny'] = []
graph['nic'] = []

print(search_name('you'))



# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         print(pivot)
#         lower = [i for i in array[1:] if i < pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(lower) + [pivot] + quicksort(greater)
#
#
# a = [10, 5, 2, 6]
# print(quicksort(a))
