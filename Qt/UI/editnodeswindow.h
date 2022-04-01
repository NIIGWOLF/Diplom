#ifndef EDITNODESWINDOW_H
#define EDITNODESWINDOW_H

#include <QWidget>

namespace Ui {
class EditNodesWindow;
}

class EditNodesWindow : public QWidget
{
    Q_OBJECT

public:
    explicit EditNodesWindow(QWidget *parent = nullptr);
    ~EditNodesWindow();

private:
    Ui::EditNodesWindow *ui;
};

#endif // EDITNODESWINDOW_H
