# ========== HELPER FUNCTION: Safe Git Wrapper ==========

run_git() {
    local description="$1"
    shift
    git "$@" > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "❌ Fatal error during: $description"
        exit 1
    fi
}