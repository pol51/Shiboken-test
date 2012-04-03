#include "foo.h"

MainW::MainW(QWidget *parent) :
  QListWidget(parent)
{
  setAlternatingRowColors(true);
}

void MainW::addLine(const QString &newLine)
{
  addItem(newLine);
}

