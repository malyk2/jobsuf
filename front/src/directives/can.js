import {hasPermissions} from '@/libs/Permissions'

function can(el, binding) {
    if (!hasPermissions(binding.value)) {
        el.style.display = 'none';
    }
}

export { can };