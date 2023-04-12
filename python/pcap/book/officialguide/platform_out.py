#!/usr/bin/env python3
import platform
print(platform.machine())
# Returns the machine type, e.g. 'AMD64'. An empty string is returned if the value cannot be determined.

print(platform.node())
# # Returns the computer’s network name (may not be fully qualified!). An empty string is returned if the value cannot be determined.

# print(platform(aliased=0, terse=0))
# # Returns a single string identifying the underlying platform with as much useful information as possible.
# # The output is intended to be human readable rather than machine parseable. It may look different on different platforms and this is intended.
# # If aliased is true, the function will use aliases for various platforms that report system names which differ from their common names, for example SunOS will be reported as Solaris. The system_alias()) function is used to implement this.
# # Setting terse to true causes the function to return only the absolute minimum information needed to identify the print(
# # Changed in version 3.8: On macOS, the function now uses mac_ver()), if it returns a non-empty release string, to get the macOS version rather than the darwin version.

print(platform.processor())
# # Returns the (real) processor name, e.g. 'amdk6'.

# # An empty string is returned if the value cannot be determined. Note that many platforms do not provide this information or simply return the same value as for machine()). NetBSD does this.

print(platform.python_build())
# # Returns a tuple (buildno, builddate) stating the Python build number and date as strings.

print(platform.python_compiler())
# # Returns a string identifying the compiler used for compiling Python.

print(platform.python_branch())
# # Returns a string identifying the Python implementation SCM branch.

print(platform.python_implementation())
# # Returns a string identifying the Python implementation. Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.

print(platform.python_revision())
# # Returns a string identifying the Python implementation SCM revision.

print(platform.python_version())
# # Returns the Python version as string 'major.minor.patchlevel'.

# # Note that unlike the Python sys.version, the returned value will always include the patchlevel (it defaults to 0).

print(platform.python_version_tuple())
# # Returns the Python version as tuple (major, minor, patchlevel) of strings.

# # Note that unlike the Python sys.version, the returned value will always include the patchlevel (it defaults to '0').

print(platform.release())
# # Returns the system’s release, e.g. '2.2.0' or 'NT'. An empty string is returned if the value cannot be determined.

print(platform.system())
# # Returns the system/OS name, such as 'Linux', 'Darwin', 'Java', 'Windows'. An empty string is returned if the value cannot be determined.

print(platform.version())

# # Returns the system’s release version, e.g. '#3 on degas'. An empty string is returned if the value cannot be determined.
print(platform.uname())