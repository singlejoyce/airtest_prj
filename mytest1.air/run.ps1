set-ExecutionPolicy RemoteSigned
$x = Split-Path -Parent $MyInvocation.MyCommand.Definition
$log_dir = $x + '\log'
$report_dir = $log_dir + '\log.html'
python -m airtest run $x --device Android:/// --log $log_dir
python -m airtest report $x --log_root $log_dir --outfile $report_dir --lang zh
pause