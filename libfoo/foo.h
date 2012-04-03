#ifndef __FOO_H__
#define __FOO_H__
 
#include <QtGui/QListWidget>

class MainW : public QListWidget
{
  Q_OBJECT
  
  public:
    MainW(QWidget *parent = NULL);
    
  public slots:
    void addLine(const QString &newLine);
};

#endif

