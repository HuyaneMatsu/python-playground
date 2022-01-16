__all__ = ('Partial', )

from functools import partial as partial_func


def partial_wrapper(parameter_count, function):
    """
    Wrapper for ``Partial.__new__` when called without `function` parameter defined as non `None`
    
    Parameters
    ----------
    parameter_count : `int`
        The expected parameter count passed to the function before calling it.
        
        This parameter is passed by a partial function wrapper, and should be passed when used.
    
    function : `GeneratorFunctionType`
        The function to wrap.
    
    Raises
    ------
    RuntimeError
    
    """
    if function is None:
        raise RuntimeError(f'`function` cannot be `None`.')
    
    return Partial(parameter_count, function=function)


class Partial:
    """
    A generator wrapper, which wraps it into a partial function.
    
    Attributes
    ----------
    function : `FunctionType`
        The wrapped function.
    generator : `GeneratorFunctionType`
        The generator returned by the function..
    parameter_count : `int`
        The expected parameter count passed to the function before calling it.
    """
    __slots__ = ('function', 'generator', 'parameter_count', )
    
    def __new__(cls, parameter_count=0, function=None):
        """
        Creates a new ``Partial`` instance from the given parameters.
        
        Parameters
        ----------
        parameter_count : `int`
            The expected parameter count passed to the function before calling it.
        function : `GeneratorFunctionType`, Optional (Keyword only)
            The function to wrap.
        
        Returns
        -------
        wrapper / self : `functools.partial` / `self`
            Returns a wrapper if `function` is not given.
        """
        if function is None:
            return partial_func(partial_wrapper, parameter_count)
        
        self = object.__new__(cls)
        self.function = function
        self.generator = None
        self.parameter_count = parameter_count
        return self
    
    
    def __call__(self, *args):
        """
        Feed a parameter to the partial func, or call it when all fed.
        
        Parameters
        ----------
        *args : `Any`
            parameters to feed to the partial function.
        
        Returns
        -------
        wrapped_value(s) / return_value : `functools.partial` / `Any` / `Any`
            The wrapped value(s) or the return of the wrapper function.
        
        Raises
        ------
        RuntimeError
            - Cannot feed parameter(s) to the wrapped function caused by bad parameter count.
            - Function didn't return on last call.
        """
        parameter_count = self.parameter_count
        if parameter_count > 0:
            if len(args) > parameter_count:
                raise RuntimeError(f'Cannot feed parameter(s) to the wrapped function caused by bad parameter count.')
            
            generator = self.generator
            if generator is None:
                generator = self.function()
                self.generator = generator
                generator.send(None)
            
            for arg in args:
                generator.send(arg)
            
            self.parameter_count = parameter_count-len(args)
            
            if len(args) == 1:
                return args[0]
            
            return args
        
        else:
            
            generator = self.generator
            if generator is None:
                generator = self.function()
                self.generator = generator
            
            try:
                generator.send(None)
            except StopIteration as err:
                args = err.args
                if args:
                    return_value = args[0]
                else:
                    return_value = None
                
                return return_value
            else:
                generator.close()
                raise RuntimeError(f'`function` didn\'t return on last call.')
    
    
    def __del__(self):
        """Clears up the generator of not yet closed."""
        generator = self.generator
        if (generator is not None):
            generator.close()
