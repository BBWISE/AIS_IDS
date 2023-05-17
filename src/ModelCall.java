import org.python.core.*;
import org.python.util.*;

public class ModelCall {
	@SuppressWarnings({ "resource", "unlikely-arg-type" })
	public static boolean modelCall() {
		
		PythonInterpreter interp = new PythonInterpreter();
		//interp.execfile("python/testingknn - Copy.py");
		interp.execfile("python/pymodule.py");
		interp.set("a", new PyInteger(3));
		interp.exec("result = square(a)");
		PyObject PyResult = interp.get("result");
		
		System.out.println(PyResult);
		
		if(PyResult.equals("attack")) {
			return false;
		}
		
		return true;
	}
}
