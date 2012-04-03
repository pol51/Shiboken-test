#ifndef __FOO_H__
#define __FOO_H__
 
#include <QtGui/QMainWindow>

class QListWidget;

class MainW : public QMainWindow
{
  Q_OBJECT
  
  public:
    MainW(QWidget *parent = NULL);
    virtual ~MainW() {}
    
  public slots:
    void addLine(const QString &newLine);
    
  protected:
    QListWidget *_list;
};

#endif

