#ifndef DIALOGRUNBUILD_H
#define DIALOGRUNBUILD_H

#include <QDialog>

namespace Ui {
class DialogRunBuild;
}

class DialogRunBuild : public QDialog
{
    Q_OBJECT

public:
    explicit DialogRunBuild(QWidget *parent = nullptr);
    ~DialogRunBuild();

private:
    Ui::DialogRunBuild *ui;
};

#endif // DIALOGRUNBUILD_H
