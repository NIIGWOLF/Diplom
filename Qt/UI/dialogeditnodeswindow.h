#ifndef DIALOGEDITNODESWINDOW_H
#define DIALOGEDITNODESWINDOW_H

#include <QDialog>

namespace Ui {
class DialogEditNodesWindow;
}

class DialogEditNodesWindow : public QDialog
{
    Q_OBJECT

public:
    explicit DialogEditNodesWindow(QWidget *parent = nullptr);
    ~DialogEditNodesWindow();

private:
    Ui::DialogEditNodesWindow *ui;
};

#endif // DIALOGEDITNODESWINDOW_H
