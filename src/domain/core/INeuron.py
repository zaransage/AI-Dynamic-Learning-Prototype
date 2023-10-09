from abc import ABCMeta
from uuid import uuid4


class INeuron(metaclass=ABCMeta):
    """
    Summary:
        This neuron takes advantage of the way AWS lambda functions work. They take a dict for parameters.
        Indeed, the firing of an AWS like Lambda function could be a good model for managing neurons.
    
    Parems:
        parameters: Dictionary of values
        identity: Random UUID for the neuron during its existence and potentially, to be saved for later use
        activation: float value intended to be used locally. This parameter is not expected to be passed in.
        weight: float value intended to be used locally. This parameter is not expected to be passed in.
        bias: float value intended to be used locally. This parameter is not expected to be passed in.
    
    Returns:
        self.state: a string or object which comprises of the identity of the neuron, the state of the neuron and the used activation derivitive.

    
    """
    def __init__(self, parameters={}) -> None:
        self.identity = uuid4()
        self.identity_neighbors = parameters["identity_neighbors"]
        self.activation = parameters["activation"]
        self.weight = ""
        self.bias = ""
        self.state = ""
 
 
    def _reference_identitiy_of_neighbors(self) -> None:
        """Look for the neurons directly in front of me, even if just one"""
        pass
    
    
    def _watch_neighbors_for_output(self):
        """This should use some kind of protocol to capture the output of the ids of the neurons adjacent and ahead of it"""
        pass
 
 
    def _process_derivitive(self) -> None:
        """Given a derivitive, weight, bias and activation, process and return the result based on the input from the previous neuron(s)"""
        pass
    
    
    def _store_state(self) -> None:
        """Future idea. Could possibly store the state in memory into a traditional matrix or other, isolated cell format"""
        pass
    
    
    def _read_state(self) -> None:
        """Future idea. Could possibly read a single matrix cell and assume that state locally"""
        pass
    
       
    def __str__(self) -> str:
        """Return an object or a string which has the identity, the computer derivitive and used activation"""
        return f"{self.identity}, {self.state}, {self.activation}"