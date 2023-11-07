from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    pq = PriorityQueue()
    pq.enqueue("Arquivo 1", ["lin 1", "lin 2", "lin 3", "lin 4"])
    pq.enqueue("Arquivo 2", ["lin 1", "lin 2", "lin 3", "lin 4", "lin 5"])
    assert pq.search(0) == "Arquivo 1"
    assert pq.search(1) == "Arquivo 2"
