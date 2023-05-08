import org.python.core.*;
import org.python.util.*;

public class ModelCall {
	@SuppressWarnings("resource")
	public static String modelCall() {
		String result = null;
		
		PythonInterpreter interp = new PythonInterpreter();
		interp.execfile("python/pymodule.py");
		interp.set("a", new PyInteger(3));
		interp.exec("result = square(a)");
		PyObject PyResult = interp.get("result");
		
		System.out.println(PyResult);
		
		return result;
	}
}
