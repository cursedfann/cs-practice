git log — история, git show — детали одного коммита/объекта, git diff — сравнение изменений между двумя состояниями
blame: dd5bfd08 (Roman 2026-10-16 23:05:07 +0300 1) f\_n = int(input("Enter a number: "))

dd5bfd08 (Roman 2026-10-16 23:05:07 +0300 2) s\_n = int(input("Enter another number: "))

dd5bfd08 (Roman 2026-10-16 23:05:07 +0300 3)

68d1f0fd (Roman 2026-10-16 23:09:50 +0300 4) print(f'summ: {f\_n + s\_n}, subtraction: {f\_n - s\_n}, multiplication: {f\_n \* s\_n}')



log:

commit 68d1f0fda68b1ab9f7772e64bbff2aaa7f74c2fd (HEAD -> main)

Author: Roman [cursedgit@gmail.com](mailto:cursedgit@gmail.com)

Date:   Fri Oct 16 23:09:50 2026 +0300



&#x20;   multiplication



commit f15d84ae7c7f1492967eb21d834854513c44a802

Author: Roman [cursedgit@gmail.com](mailto:cursedgit@gmail.com)

Date:   Fri Oct 16 23:09:17 2026 +0300



&#x20;   subtraction



commit dd5bfd08efcb93072e2eccfd1b4d5ae1c9b562a2

Author: Roman [cursedgit@gmail.com](mailto:cursedgit@gmail.com)

Date:   Fri Oct 16 23:05:07 2026 +0300



&#x20;   sum

git restore lab03/calc.py:



&#x09;Возвращает файл из индекса (если делал git add) или из HEAD.



&#x09;Незастейдженные правки теряются, застейдженные — сохраняются.

&#x09;

&#x09;HEAD и история не трогаются.



git restore --source=HEAD\~2 lab03/calc.py:



&#x09;Возвращает файл из коммита HEAD\~2 (2 коммита назад).



&#x09;Все текущие правки (и staged, и unstaged) теряются.



&#x09;HEAD не двигается, файл просто становится «старой версией» → в git status как изменённый.

reset --hard — это «перемотать ветку назад», а restore — «починить отдельный файл».



Почему revert безопаснее в опубликованной истории



reset переписывает историю: коммиты, на которые уже могли опираться другие, пропадают. У коллег ветка разойдётся → придётся push --force, что ломает их работу.



revert добавляет новый коммит, который отменяет изменения указанного. История остаётся линейной и общей, push обычный, ничего не ломается.



ветка — живой указатель для работы, тег — неподвижная закладка на конкретный коммит.

