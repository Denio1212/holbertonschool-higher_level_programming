# Here be all the stuff..!
So for task 0 we need all the test cases and such.

> Moving on to the second task, or 1 since they start from 0

*All we need to do for the first task is make a class that will be
the blueprint for all future objects, this will be
everything that they will share together, and the subsequent objects will carry
these and specialized traits.*

> We are required to make a class attribute that will hold the number of objects created
> and we need to manage the id of these objects. If said id is not None we wil overwrite it and simply replace it.
> 
> If it is indeed None we will make a new value and assign it into the id and increment the instances.

```
# The code for the above

if id is not None:
    self.id = id
else:
    Base.__nb_objects += 1
    self.id = Base.__nb_objects
```
**That concludes the first/second tasks**

