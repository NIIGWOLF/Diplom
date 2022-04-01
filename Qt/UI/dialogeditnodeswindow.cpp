#include "dialogeditnodeswindow.h"
#include "ui_dialogeditnodeswindow.h"

DialogEditNodesWindow::DialogEditNodesWindow(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::DialogEditNodesWindow)
{
    ui->setupUi(this);
}

DialogEditNodesWindow::~DialogEditNodesWindow()
{
    delete ui;
}
