from fastapi import FastAPI

app = FastAPI(
    title="Student Attendance Tracker",
    description="Local Student Attendance Management System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Student Attendance Tracker API is running"
    }


@app.get("/api/health")
def health():
    return {
        "status": "healthy"
    }

from pathlib import Path

source = Path("/run/media/nikhil/work 2/Website/frontend/student_dashboard.html")
html = source.read_text(encoding="utf-8")

needle = '''                            <!-- Quick Action Buttons -->
                            <div class="flex gap-2">
                                <button onclick="toggleEditModal()" class="flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-sm font-semibold shadow-sm transition-all">
                                    <i data-lucide="edit-3" class="w-4 h-4"></i>
                                    Edit Info
                                </button>
                            </div>
                        </div>'''

replacement = '''                            <!-- Quick Action Buttons -->
                            <div class="flex gap-2">
                                <button onclick="toggleEditModal()" class="flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-sm font-semibold shadow-sm transition-all">
                                    <i data-lucide="edit-3" class="w-4 h-4"></i>
                                    Edit Info
                                </button>
                            </div>

                            <!-- Student QR Code -->
                            <div class="shrink-0 flex flex-col items-center gap-2 rounded-2xl border border-slate-200 bg-white p-3 shadow-sm">
                                <p class="text-xs font-bold uppercase tracking-wider text-slate-500">Student QR Code</p>
                                <img
                                    id="studentQrCode"
                                    src="/qr.png"
                                    alt="Student QR code"
                                    class="h-32 w-32 rounded-lg object-contain"
                                    onerror="this.hidden=true; document.getElementById('qrMissingMessage').classList.remove('hidden');"
                                >
                                <p id="qrMissingMessage" class="hidden max-w-[8rem] text-center text-xs text-rose-600">
                                    QR image not found. Place qr.png in the frontend folder.
                                </p>
                                <a href="/qr.png" download="student-qr.png"
                                   class="text-xs font-semibold text-indigo-600 hover:text-indigo-800">
                                    Download QR
                                </a>
                            </div>
                        </div>'''

if needle not in html:
    raise ValueError("Could not find the profile header section to insert the QR code.")

updated = html.replace(needle, replacement, 1)
output = Path("/mnt/data/student_dashboard_with_qr.html")
output.write_text(updated, encoding="utf-8")

print(f"Updated dashboard saved: {output}")
print("QR image reference: /qr.png")
print("Place your qr.png file in the same frontend directory as this HTML file.")

