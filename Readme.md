# Yurlungur

|       | Windows | Unix | code |
| ----- | ------ | --- | --- |
| OS | [![Build status](https://ci.appveyor.com/api/projects/status/46vinb8jd1jbbhdg?svg=true)](https://ci.appveyor.com/project/sho7noka/yurlungur) | [![Build Status](https://travis-ci.org/sho7noka/Yurlungur.svg?branch=dev)](https://travis-ci.org/sho7noka/Yurlungur) | [![codecov](https://codecov.io/gh/sho7noka/Yurlungur/branch/dev/graph/badge.svg)](https://codecov.io/gh/sho7noka/Yurlungur) |


universal scripting environment with Python which Maya, Houdini and Blender.

## summary
DCC tool scripting is almost used Python, but these api isn't similarly anything.
If you make lightweight tool, need to remember each application manners.
Yurlungur is common interface which adapted each application for universal wrapper.

Yurlungur is inspired by [PyMEL](https://github.com/LumaPictures/pymel).

### future
* HOM (Houdini Object Model) like command wrapper.
* PySide & PyQt shorten accessor.
* Useful py-snippet for Game&Film technical artist.

### availables
|       | Node | Attribute | Geom |
| ---- | --- | --- | --- |
| Maya | ○ | ○ | ☓ |
| Houdini | ○ | ○ | ☓ |
| Blender | ○ | ○ | ☓ |
| Substance | ○ | ○ | - |
| [Gaffer](http://www.gafferhq.org/documentation/0.50.0.0/Reference/ScriptingReference/CommonOperations/index.html) | - | - | - |
| [Unreal](https://docs.unrealengine.com/en-US/Editor/Scripting-and-Automating-the-Editor/Scripting-the-Editor-using-Python) | - | - | - |



### Installing
```bash
pipenv install yurlungur
```

#### optional
If you use Unreal or Standalone for full supports, Yurlungur require `PySide` module.

```bash
pipenv install pyside
```

### semantics

```python
# Blender
bpy.data.objects["foo"].bar = 1
```

```mel
// MEL
setAttr "foo.bar" 1;
```

```python
# yurlungur
import yurlungur as yr
yr.YNode("foo").bar.set(1)
```

## TODO
- [x] basic api
- [x] github.io
- [ ] unreal

## contribution
lets see [CONTRIBUTING](./CONTRIBUTING.md).


## License
Yurlungur is [MIT](./LICENSE.md) License.
