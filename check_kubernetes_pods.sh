if kubectl get pod hello-app-deployment-6b6dbffdd6-74fpl | grep "Running"; then
    echo "OK - Pods are running"
    exit 0
else
    echo "CRITICAL - Some pods are not running"
    exit 2
fi
