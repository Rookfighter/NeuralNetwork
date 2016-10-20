import neunet.neuron as neuron
import neunet.training as training
import sys

if __name__ == '__main__':
    network = neuron.NeuralNetwork(1)
    network.addNeuron(0, 'jump', [1, 1, 1, 1], 0.5)
    network.addNeuron(0, 'jump', [1, 1, 1, 1], 0.5)
    network.addNeuron(0, 'jump', [1, 1, 1, 1], 0.5)
    network.addNeuron(0, 'jump', [1, 1, 1, 1], 0.5)
    network.addNeuron(0, 'jump', [1, 1, 1, 1], 0.5)
    network.addNeuron(0, 'jump', [1, 1, 1, 1], 0.5)
    network.addNeuron(0, 'jump', [1, 1, 1, 1], 0.5)
    network.addNeuron(0, 'jump', [1, 1, 1, 1], 0.5)
    network.addNeuron(0, 'jump', [1, 1, 1, 1], 0.5)
    network.addNeuron(0, 'jump', [1, 1, 1, 1], 0.5)


    trainer = training.Binary2UnaryTrainer(network, 0.2)
    trainer.load('mytraining.txt')
    trainer.train()

    print('Give me a number: ')
    line = sys.stdin.readline().strip()
    while line:
        inVals = training.binStrToVals(line)
        inVals = [inVals for _ in network._layers[0]]
        outVals = network.compute(inVals)
        print('-- {0}'.format(outVals))

        print('Give me a number: ')
        line = sys.stdin.readline().strip()
