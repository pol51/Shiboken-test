#include "foo.h"

#include <QtGui/QListWidget>

MainW::MainW(QWidget *parent) :
  QMainWindow(parent)
{
  _list = new QListWidget(this);
  _list->setAlternatingRowColors(true);
  setCentralWidget(_list);
}

void MainW::addLine(const QString &newLine)
{
  _list->addItem(newLine);
}
