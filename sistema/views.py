import platform
from django.shortcuts import render
from django.http import JsonResponse

def collect_metrics():
    data = {
        "cpu_percent": None,
        "cpu_count_logical": None,
        "cpu_count_physical": None,
        "memory_total_gb": None,
        "memory_used_gb": None,
        "memory_percent": None,
        "disk_total_gb": None,
        "disk_used_gb": None,
        "disk_free_gb": None,
        "os": None,
        "platform": None,
        "error": None,
    }

    try:
        import psutil
    except Exception as e:
        data["error"] = f"psutil import error: {e}"
        return data

    try:
        data["cpu_percent"] = psutil.cpu_percent(interval=0.1)
        data["cpu_count_logical"] = psutil.cpu_count(logical=True)
        try:
            data["cpu_count_physical"] = psutil.cpu_count(logical=False)
        except Exception:
            data["cpu_count_physical"] = None

        vm = psutil.virtual_memory()
        data["memory_total_gb"] = round(vm.total / (1024**3), 2)
        data["memory_used_gb"] = round((vm.total - vm.available) / (1024**3), 2)
        data["memory_percent"] = vm.percent

        du = psutil.disk_usage('/')
        data["disk_total_gb"] = round(du.total / (1024**3), 2)
        data["disk_used_gb"] = round(du.used / (1024**3), 2)
        data["disk_free_gb"] = round(du.free / (1024**3), 2)

        data["os"] = platform.system() + " " + platform.release()
        data["platform"] = platform.platform()

    except Exception as ex:
        data["error"] = f"psutil runtime error: {ex}"

    return data


def index(request):
    metrics = collect_metrics()
    return render(request, 'sistema/index.html', {'metrics': metrics})


def api_metrics(request):
    metrics = collect_metrics()
    return JsonResponse(metrics, safe=True)
