from LoadBalancer import RRLoadBalancer
from input_parsers import parse_nodes_config
from Feeder import FileFeeder
from taskdispatcher import TaskDispathcer
from node_worker import NodeGenericWorker

def main():
    nodes_list = list(parse_nodes_config(r'tests\files\nodes1.config'))
    feeder = FileFeeder(r"tests\files\tasks1.config")

    loadbalancer = RRLoadBalancer(nodes_list)
    dispatcher = TaskDispathcer(feeder, loadbalancer)

    workers_list = []
    for node in nodes_list:
        worker = NodeGenericWorker(node)
        workers_list.append(worker)
        worker.start()

    dispatcher.dispatch_tasks()
    
    for worker in workers_list:
        worker.join()


if __name__ == "__main__":
    main()