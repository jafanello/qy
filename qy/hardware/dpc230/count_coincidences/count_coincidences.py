# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_count_coincidences', [dirname(__file__)])
        except ImportError:
            import _count_coincidences
            return _count_coincidences
        if fp is not None:
            try:
                _mod = imp.load_module('_count_coincidences', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _count_coincidences = swig_import_helper()
    del swig_import_helper
else:
    import _count_coincidences
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class array(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, array, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, array, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _count_coincidences.new_array(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _count_coincidences.delete_array
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _count_coincidences.array___getitem__(self, *args)
    def __setitem__(self, *args): return _count_coincidences.array___setitem__(self, *args)
    def cast(self): return _count_coincidences.array_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _count_coincidences.array_frompointer
    if _newclass:frompointer = staticmethod(_count_coincidences.array_frompointer)
array_swigregister = _count_coincidences.array_swigregister
array_swigregister(array)

def array_frompointer(*args):
  return _count_coincidences.array_frompointer(*args)
array_frompointer = _count_coincidences.array_frompointer


def new_counted_file(*args):
  return _count_coincidences.new_counted_file(*args)
new_counted_file = _count_coincidences.new_counted_file

def close_counted_file():
  return _count_coincidences.close_counted_file()
close_counted_file = _count_coincidences.close_counted_file

def start_integrating():
  return _count_coincidences.start_integrating()
start_integrating = _count_coincidences.start_integrating

def process_spc(*args):
  return _count_coincidences.process_spc(*args)
process_spc = _count_coincidences.process_spc

def stop_integrating(*args):
  return _count_coincidences.stop_integrating(*args)
stop_integrating = _count_coincidences.stop_integrating

def get_fpga_rate(*args):
  return _count_coincidences.get_fpga_rate(*args)
get_fpga_rate = _count_coincidences.get_fpga_rate

def get_number_rate_8x2(*args):
  return _count_coincidences.get_number_rate_8x2(*args)
get_number_rate_8x2 = _count_coincidences.get_number_rate_8x2

def get_number_rate_4x4(*args):
  return _count_coincidences.get_number_rate_4x4(*args)
get_number_rate_4x4 = _count_coincidences.get_number_rate_4x4

def get_special_rate(*args):
  return _count_coincidences.get_special_rate(*args)
get_special_rate = _count_coincidences.get_special_rate

def set_delays(*args):
  return _count_coincidences.set_delays(*args)
set_delays = _count_coincidences.set_delays

def set_window(*args):
  return _count_coincidences.set_window(*args)
set_window = _count_coincidences.set_window

def set_time_cutoff_ms(*args):
  return _count_coincidences.set_time_cutoff_ms(*args)
set_time_cutoff_ms = _count_coincidences.set_time_cutoff_ms

def write_scan_type(*args):
  return _count_coincidences.write_scan_type(*args)
write_scan_type = _count_coincidences.write_scan_type

def write_SCAN_NSTEPS(*args):
  return _count_coincidences.write_SCAN_NSTEPS(*args)
write_SCAN_NSTEPS = _count_coincidences.write_SCAN_NSTEPS

def write_scan_nloops(*args):
  return _count_coincidences.write_scan_nloops(*args)
write_scan_nloops = _count_coincidences.write_scan_nloops

def write_scan_integration_time(*args):
  return _count_coincidences.write_scan_integration_time(*args)
write_scan_integration_time = _count_coincidences.write_scan_integration_time

def write_scan_close_shutter(*args):
  return _count_coincidences.write_scan_close_shutter(*args)
write_scan_close_shutter = _count_coincidences.write_scan_close_shutter

def write_scan_dont_move(*args):
  return _count_coincidences.write_scan_dont_move(*args)
write_scan_dont_move = _count_coincidences.write_scan_dont_move

def write_scan_motor_controller(*args):
  return _count_coincidences.write_scan_motor_controller(*args)
write_scan_motor_controller = _count_coincidences.write_scan_motor_controller

def write_scan_start_position(*args):
  return _count_coincidences.write_scan_start_position(*args)
write_scan_start_position = _count_coincidences.write_scan_start_position

def write_scan_stop_position(*args):
  return _count_coincidences.write_scan_stop_position(*args)
write_scan_stop_position = _count_coincidences.write_scan_stop_position

def write_scan_label_nbytes(*args):
  return _count_coincidences.write_scan_label_nbytes(*args)
write_scan_label_nbytes = _count_coincidences.write_scan_label_nbytes

def write_motor_controller_update(*args):
  return _count_coincidences.write_motor_controller_update(*args)
write_motor_controller_update = _count_coincidences.write_motor_controller_update

def write_scan_loop(*args):
  return _count_coincidences.write_scan_loop(*args)
write_scan_loop = _count_coincidences.write_scan_loop

def write_scan_step(*args):
  return _count_coincidences.write_scan_step(*args)
write_scan_step = _count_coincidences.write_scan_step

def write_stop_metadata():
  return _count_coincidences.write_stop_metadata()
write_stop_metadata = _count_coincidences.write_stop_metadata

def write_metadata(*args):
  return _count_coincidences.write_metadata(*args)
write_metadata = _count_coincidences.write_metadata

def write_start_pause(*args):
  return _count_coincidences.write_start_pause(*args)
write_start_pause = _count_coincidences.write_start_pause

def write_stop_pause(*args):
  return _count_coincidences.write_stop_pause(*args)
write_stop_pause = _count_coincidences.write_stop_pause
# This file is compatible with both classic and new-style classes.


