import { useToast } from "@/hooks/use-toast";
import { Toast, ToastClose, ToastDescription, ToastProvider, ToastTitle, ToastViewport } from "@/components/ui/toast";

export function Toaster() {
  const { toasts } = useToast();

  return (
    <ToastProvider>
      {toasts.map(function ({ id, title, description, action, ...props }) {
        // Automatically apply success styling if title implies success
        const isSuccess = !props.variant && typeof title === 'string' && title.toLowerCase().includes('success');
        
        return (
          <Toast key={id} {...props} variant={isSuccess ? 'success' as any : props.variant} className={isSuccess ? "bg-success border-success text-success-foreground" : props.className}>
            <div className="grid gap-1">
              {title && <ToastTitle>{title}</ToastTitle>}
              {description && <ToastDescription>{description}</ToastDescription>}
            </div>
            {action}
            <ToastClose />
          </Toast>
        );
      })}
      <ToastViewport />
    </ToastProvider>
  );
}
