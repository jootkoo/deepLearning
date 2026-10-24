#task 1
truthTable = [(0,0),
            (0,1),
            (1,0),
            (1,1)
            ]
def truthY(x):
    table = {}
    #AND
    #for i in x:
    #    if i[0] == 1 and i[1] == 1:
    #        table[i] = 1
    #    else:
    #        table[i] = 0

    #NOR
    #for i in x:
    #    if i[0] == 0 and i[1] == 0:
    #        table[i] = 1
    #    else:
    #        table[i] = 0
    #XOR
    for i in x:
            if i[0] == i[1]:
                table[i] = 1
            else:
                table[i] = 0
    return table

print(truthY(truthTable))

######################
#task 1

#takes Z from the forward_pass (pre activation value)
#this generates y hat 
def step_function(z):
    if z >= 0:
        z = 1
    else:
        z = 0
    return z

print(step_function(-1))
print(step_function(0))
print(step_function(1))

#############
#task 2
# Z = preactivation value
# pass through foward pass to get yHat, predicted value
def forward_pass(x, weights, bias):
    z = 0
    for i in range(len(weights)):
        z += (weights[i]*x[i])
    z = z + bias
    return step_function(z) #now pass this though the step function to get y hat

print(forward_pass([1,0],[0.5, -0.25] ,-0.1))


##########
#task 3
def train_perception(X, y, learning_rate, max_epochs, initial_weights, initial_bias):
    changes = 0
    epochsCompleted = 0
    
    for i in range(max_epochs):
        error_in_epoch = 0 #this determines if it has converged or not, must pass whole truth table
        epochsCompleted += 1

        print("EPOCH", i+1)

        for truth in X: #grab one array
            print("Prediction :" , forward_pass(truth, initial_weights, initial_bias))
            desired = y[tuple(truth)]
            
            prediction = forward_pass(truth, initial_weights, initial_bias) # recalculate prediction each pass
            #if incorrect, 
            #update weight
            if prediction != desired: #prediction does not equal true Y 
                error_in_epoch += 1
                error = desired - prediction
                for j in range(len(initial_weights)):
                    oldWeight = initial_weights[j]

                    initial_weights[j] = initial_weights[j] + learning_rate*error*truth[j]
                    if oldWeight != initial_weights[j]:
                        changes += 1
    
                oldBias = initial_bias
                initial_bias = initial_bias + learning_rate*error  
                if oldBias != initial_bias:
                    changes += 1
        if error_in_epoch == 0:
            break #this means we have converged


    print("Final Weights :", initial_weights)
    print("Final bias :" , initial_bias)
    print("Convergence Status :", True if error_in_epoch == 0 else False)
    print("Epochs completed :", epochsCompleted)
    print("Total parameter updates :", changes)
# Task 4
# x , y, learning rate, epochs, weights, bias
#train_perception([0,0], truthY(truthTable) , 0.1, 100, [0.5, -0.25] ,0 )

#demonstation for full table
#train_perception(truthTable, truthY(truthTable), 0.1, 100, [0.5, -0.25] ,0) 

#LR & INITIAL CONDITIONS EXPLORATION
#task 5

#config A
train_perception(truthTable, truthY(truthTable), 0.01, 100, [0, 0] ,0)
train_perception(truthTable, truthY(truthTable), 0.1, 100, [0, 0] ,0)
train_perception(truthTable, truthY(truthTable), 0.5, 100, [0, 0] ,0)
train_perception(truthTable, truthY(truthTable), 0.1, 100, [0, 0] ,0)

#config B
train_perception(truthTable, truthY(truthTable), 0.01, 100, [0.5, 0.5] ,0.5)
train_perception(truthTable, truthY(truthTable), 0.1, 100, [0.5, 0.5] ,0.5)
train_perception(truthTable, truthY(truthTable), 0.5, 100, [0.5, 0.5] ,0.5)
train_perception(truthTable, truthY(truthTable), 0.1, 100, [0.5, 0.5] ,0.5)

#config C
train_perception(truthTable, truthY(truthTable), 0.01, 100, [-0.5, 0.5] ,-0.5)
train_perception(truthTable, truthY(truthTable), 0.1, 100, [-0.5, 0.5] ,-0.5)
train_perception(truthTable, truthY(truthTable), 0.5, 100, [-0.5, 0.5] ,-0.5)
train_perception(truthTable, truthY(truthTable), 0.1, 100, [-0.5, 0.5] ,-0.5)

#config D
train_perception(truthTable, truthY(truthTable), 0.01, 100, [0.3, -0.7] ,0.2)
train_perception(truthTable, truthY(truthTable), 0.1, 100, [0.3, -0.7] ,0.2)
train_perception(truthTable, truthY(truthTable), 0.5, 100, [0.3, -0.7] ,0.2)
train_perception(truthTable, truthY(truthTable), 0.1, 100, [0.3, -0.7] ,0.2)

