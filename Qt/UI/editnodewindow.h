#ifndef EDITNODEWINDOW_H
#define EDITNODEWINDOW_H

#include <QMainWindow>

namespace Ui {
class EditNodeWindow;
}

class EditNodeWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit EditNodeWindow(QWidget *parent = nullptr);
    ~EditNodeWindow();

private:
    Ui::EditNodeWindow *ui;
};

#endif // EDITNODEWINDOW_H
