===================================
tool conf
===================================
yurlungur tool scripting tips.


Log
-------------------------------
print statement is not available in Python3.
Also IronPython is not bind with __future__ modules.

print 文は Python3 ではエラーになり、それを回避するための
__future__ モジュールも Unity Asset 内の IronPython ではサポートされないため、
`yurlungur.log(*args)` の使用をお勧めします。


.. code-block:: python

    yurlungur.log(*args)

内部処理に pformat を使っているため、ログが見切れるような
長いリストでも視認性は損なわれません。

LogHandler をそれぞれのアプリケーションから継承し、一貫したインターフェースで
出力レベルの制御をします。


UndoGroup
-------------------------------
contextManager で制御されたUndoGroup で
アプリケーション側のUndoで操作を巻き戻すことが出来ます。

.. code-block:: python

    with yr.UndoGroup:
        yr.YNode("hoge").delete()


もしUndoGroupでインデントを囲わないスクリプト処理をした場合、
ひとつひとつ undo で戻さなければなりません。


GUI
--------------------------------
Qt.py をラッピングしているので、Maya/Houdini といった
大型スタジオで使われるアプリケーションのバージョンを気にすることなく
Python から Qt を使うことが出来ます。


.. code-block:: python

    widget = QWidget()
    yr.qt.show(widget)


ゲームエンジンはQtを内蔵しません。
別途 pip インストールするか、env モジュールでアプリケーションを切り分けて、
meta モジュールからそれぞれネイティブの ui モジュールを参照して下さい。